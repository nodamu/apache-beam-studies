import apache_beam as beam


def SplitRow(element):
    return element.split(',')


p = beam.Pipeline()

# Input Pcollection

input_collection = (
        p
        | "Read from file" >> beam.io.ReadFromText('structure_of_beam_apps/dept-data.txt')
        | "Split rows" >> beam.Map(SplitRow)
)

accounts_count = (
        input_collection
        | "Get all Accounts dept person" >> beam.Filter(lambda record : record[3] == 'Accounts')
        | "Pair each accounts employee name with 1" >> beam.Map(lambda record : (record[1],1))
        | "Group and sum Accounts" >> beam.CombinePerKey(sum)
        | "Write results for accounts" >> beam.io.WriteToText('structure_of_beam_apps/data/Account')
)

hr_count = (
    input_collection
    | "Get all HR dept persons" >> beam.Filter(lambda record : record[3] == 'HR')
    | "Pair each hr employee name with 1" >> beam.Map(lambda record : (record[1], 1))
    | "Group and sum HR" >> beam.CombinePerKey(sum)
    | "Write results for HR" >> beam.io.WriteToText('structure_of_beam_apps/data/HR')
)

p.run()