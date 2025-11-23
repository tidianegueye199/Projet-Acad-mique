import pandas as pd
import xlrd

"""
class data_scrap:

    def chemin(fichier, sheet):

        workbook = xlrd.open_workbook(fichier)

        worksheet = workbook.sheet_by_name(sheet)

        return worksheet

    def data_frame(fichier, ligne_debut, col_debut):
        var_names = []
        for it_col in range(4, 4+63, 1):
            data = fichier.cell_value(ligne_debut, it_col)
            var_names.append(data)

        resultat_data = [var_names]
        for curr_row in range(ligne_debut + 1, ligne_debut+9, 1):
            row_data = []
            for curr_col in range(col_debut, col_debut+63, 1):
                data = fichier.cell_value(curr_row, curr_col)
                #print(data)
                row_data.append(data)
            resultat_data.append(row_data)

        variables = ["ges", "unite", "a1960", "a1961", "a1962", "a1963", "a1964", "a1965", "a1966", "a1967",
 "a1968", "a1969", "a1970", "a1971", "a1972", "a1973", "a1974", "a1975", "a1976", "a1977", "a1978", 
 "a1979", "a1980", "a1981", "a1982", "a1983", "a1984", "a1985", "a1986", "a1987", "a1988", "a1989",
 "a1990", "a1991", "a1992", "a1993", "a1994", "a1995", "a1996", "a1997", "a1998", "a1999", "a2000",
 "a2001", "a2002", "a2003", "a2004", "a2005", "a2006", "a2007", "a2008", "a2009", "a2010", "a2011",
 "a2012", "a2013", "a2014", "a2015", "a2016", "a2017", "a2018", "a2019", "a2020"]

        variables_supprimees = ["a1960", "a1961", "a1962", "a1963", "a1964", "a1965", "a1966", "a1967",
"a1968", "a1969", "a1970", "a1971", "a1972", "a1973", "a1974", "a1975", "a1976", "a1977", "a1978",
"a1979", "a1980", "a1981", "a1982", "a1983", "a1984", "a1985", "a1986", "a1987", "a1988", "a1989"]
        
        df = pd.DataFrame(resultat_data, columns = variables)
        df = df.drop(variables_supprimees, axis=1)
        return df

"""
class data_scrap:

    def chemin(fichier, sheet):

        workbook = xlrd.open_workbook(fichier)

        worksheet = workbook.sheet_by_name(sheet)

        return worksheet

    def data_frame(fichier, ligne_debut, col_debut):
        var_names = []
        for it_ligne in range(ligne_debut-1, ligne_debut+9, 1):
            data = fichier.cell_value(it_ligne, col_debut + 63 -31)
            var_names.append(data)

        resultat_data = [var_names]
        for curr_col in range(col_debut + 63 -30, col_debut+63, 1):
            col_data = []
            for curr_row in range(ligne_debut-1, ligne_debut+9, 1):
                data = fichier.cell_value(curr_row, curr_col)
                #print(data)
                col_data.append(data)
            resultat_data.append(col_data)

        variables = ["annee", "CO2", "CO2e", "CH4","N2O","HFC","PFC","SF6","NF3","Gaz_fluores"]

        
        df = pd.DataFrame(resultat_data, columns = variables)
        return df