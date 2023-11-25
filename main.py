import csv

ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []


def load_list_data(lst, csv_file, column):
    with open(csv_file) as csv_info:
        csv_dict = csv.DictReader(csv_info)
        for row in csv_dict:
            lst.append(row[column])
        return lst


load_list_data(ages, 'insurance.csv', 'age')
load_list_data(sexes, 'insurance.csv', 'sex')
load_list_data(bmis, 'insurance.csv', 'bmi')
load_list_data(num_children, 'insurance.csv', 'children')
load_list_data(smoker_statuses, 'insurance.csv', 'smoker')
load_list_data(regions, 'insurance.csv', 'region')
load_list_data(insurance_charges, 'insurance.csv', 'charges')


class PatientsInfo:
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children, patients_smoker_statuses,
                 patients_regions, patients_insurance_charges, ):
        self.patients_dictionary = None
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_insurance_charges = patients_insurance_charges

    def analyze_ages(self):
        sum_of_ages = 0

        for age in self.patients_ages:
            sum_of_ages += int(age)

        return "Average Patient Age: " + str(round(sum_of_ages / len(self.patients_ages), 2)) + " years"

    def analyze_sex(self):
        males = 0
        females = 0

        for sex in self.patients_sexes:
            if sex == "female":
                females += 1
            else:
                males += 1
        print("Count for female: ", females)
        print("Count for male: ", males)

    def unique_regions(self):
        unique_region = []

        for region in self.patients_regions:
            if region not in unique_region:
                unique_region.append(region)

        return unique_region

    def average_charges(self):
        total_charges = 0

        for charge in self.patients_insurance_charges:
            total_charges += float(charge)

        return ("Average Yearly Medical Insurance Charges: " +
                str(round(total_charges / len(self.patients_insurance_charges), 2)) + " dollars.")

    def create_dictionary(self):
        self.patients_dictionary = {"age": [int(age) for age in self.patients_ages],
                                    "sex": self.patients_sexes,
                                    "bmi": self.patients_bmis,
                                    "children_number": self.patients_num_children,
                                    "smoker_status": self.patients_smoker_statuses,
                                    "region": self.patients_regions,
                                    "charges": self.patients_insurance_charges
                                    }
        return self.patients_dictionary


patient_info = PatientsInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)

import csv

ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []


def load_list_data(lst, csv_file, column):
    with open(csv_file) as csv_info:
        csv_dict = csv.DictReader(csv_info)
        for row in csv_dict:
            lst.append(row[column])
        return lst


load_list_data(ages, 'insurance.csv', 'age')
load_list_data(sexes, 'insurance.csv', 'sex')
load_list_data(bmis, 'insurance.csv', 'bmi')
load_list_data(num_children, 'insurance.csv', 'children')
load_list_data(smoker_statuses, 'insurance.csv', 'smoker')
load_list_data(regions, 'insurance.csv', 'region')
load_list_data(insurance_charges, 'insurance.csv', 'charges')


class PatientsInfo:
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children, patients_smoker_statuses,
                 patients_regions, patients_insurance_charges, ):
        self.patients_dictionary = None
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_insurance_charges = patients_insurance_charges

    def analyze_ages(self):
        sum_of_ages = 0

        for age in self.patients_ages:
            sum_of_ages += int(age)

        return "Average Patient Age: " + str(round(sum_of_ages / len(self.patients_ages), 2)) + " years"

    def analyze_sex(self):
        males = 0
        females = 0

        for sex in self.patients_sexes:
            if sex == "female":
                females += 1
            else:
                males += 1
        print("Count for female: ", females)
        print("Count for male: ", males)

    def unique_regions(self):
        unique_region = []

        for region in self.patients_regions:
            if region not in unique_region:
                unique_region.append(region)

        return unique_region

    def average_charges(self):
        total_charges = 0

        for charge in self.patients_insurance_charges:
            total_charges += float(charge)

        return ("Average Yearly Medical Insurance Charges: " +
                str(round(total_charges / len(self.patients_insurance_charges), 2)) + " dollars.")

    def create_dictionary(self):
        self.patients_dictionary = {"age": [int(age) for age in self.patients_ages],
                                    "sex": self.patients_sexes,
                                    "bmi": self.patients_bmis,
                                    "children_number": self.patients_num_children,
                                    "smoker_status": self.patients_smoker_statuses,
                                    "region": self.patients_regions,
                                    "charges": self.patients_insurance_charges
                                    }
        return self.patients_dictionary


patient_info = PatientsInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)

import csv

ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []


def load_list_data(lst, csv_file, column):
    with open(csv_file) as csv_info:
        csv_dict = csv.DictReader(csv_info)
        for row in csv_dict:
            lst.append(row[column])
        return lst


load_list_data(ages, 'insurance.csv', 'age')
load_list_data(sexes, 'insurance.csv', 'sex')
load_list_data(bmis, 'insurance.csv', 'bmi')
load_list_data(num_children, 'insurance.csv', 'children')
load_list_data(smoker_statuses, 'insurance.csv', 'smoker')
load_list_data(regions, 'insurance.csv', 'region')
load_list_data(insurance_charges, 'insurance.csv', 'charges')


class PatientsInfo:
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children, patients_smoker_statuses,
                 patients_regions, patients_insurance_charges, ):
        self.patients_dictionary = None
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_insurance_charges = patients_insurance_charges

    def analyze_ages(self):
        sum_of_ages = 0

        for age in self.patients_ages:
            sum_of_ages += int(age)

        return "Average Patient Age: " + str(round(sum_of_ages / len(self.patients_ages), 2)) + " years"

    def analyze_sex(self):
        males = 0
        females = 0

        for sex in self.patients_sexes:
            if sex == "female":
                females += 1
            else:
                males += 1
        print("Count for female: ", females)
        print("Count for male: ", males)

    def unique_regions(self):
        unique_region = []

        for region in self.patients_regions:
            if region not in unique_region:
                unique_region.append(region)

        return unique_region

    def average_charges(self):
        total_charges = 0

        for charge in self.patients_insurance_charges:
            total_charges += float(charge)

        return ("Average Yearly Medical Insurance Charges: " +
                str(round(total_charges / len(self.patients_insurance_charges), 2)) + " dollars.")

    def create_dictionary(self):
        self.patients_dictionary = {"age": [int(age) for age in self.patients_ages],
                                    "sex": self.patients_sexes,
                                    "bmi": self.patients_bmis,
                                    "children_number": self.patients_num_children,
                                    "smoker_status": self.patients_smoker_statuses,
                                    "region": self.patients_regions,
                                    "charges": self.patients_insurance_charges
                                    }
        return self.patients_dictionary


patient_info = PatientsInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)

print(patient_info.analyze_ages())
print(patient_info.analyze_sex())
print("Unique Regions:", patient_info.unique_regions())
print(patient_info.average_charges())