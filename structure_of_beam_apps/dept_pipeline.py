import apache_beam as beam


def SplitRow(element):
    return element.split(',')

def filtering(record):
  return record[3] == 'Accounts'


with beam.Pipeline() as p1:

  attendance_count = (
    
   p1
    |"Read from a file" >> beam.io.ReadFromText('dept-data.txt')
    |"Map transform" >> beam.Map(lambda record: record.split(','))
    |beam.Filter(lambda record: record[3] == 'Accounts') 
    |beam.Map(lambda record: (record[1], 1))
    |beam.CombinePerKey(sum) 
    |beam.io.WriteToText('data/output_new_final')
  
)


