import xml.dom.minidom

def parse_xml(file_name):

  doc = xml.dom.minidom.parse(file_name)

  company = doc.documentElement

  employees = company.getElementsByTagName("employee")

  for employee in employees:
    name = employee.getElementsByTagName("name")[0].childNodes[0].data
    salary = employee.getElementsByTagName("salary")[0].childNodes[0].data
    print("Tên: ", name)
    print("Lương: ", salary)
    print("-------------------")

parse_xml("sample.xml")