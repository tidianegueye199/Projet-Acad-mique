import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf


def forward_selected(data, response, criterion):
      """Linear model designed by forward selection.
      References:
      -----------
      An Introduction to Statistical Learning with Applications in R -
      G. James, D. Witten, T. Hastie and R. Tibshirani (2021) - Algorithm 6.2
      Parameters:
      -----------
      data : pandas DataFrame with all possible predictors and response
      response: string, name of response column in data
      Returns:
      --------
      model: an "optimal" fitted statsmodels linear model
      with an intercept selected by forward selection
      """
      predictors = set(data.columns)
      predictors.remove(response)
      best_models = []
      selected = []
      while len(predictors) > 0:
         models = {}
         for candidate in predictors:
            formula = f"{response} ~ 1 + {'+'.join(selected + [candidate])}"
            models[candidate] = smf.ols(formula, data).fit()
         var, model = max(models.items(), key=lambda x: x[1].rsquared)
         selected.append(var)
         predictors.remove(var)
         best_models.append(model)
        
         

      if criterion == 'aic':
         model_select = np.argmin([model.aic for model in best_models])
      elif criterion == 'bic':
         model_select = np.argmin([model.bic for model in best_models])
      elif criterion == 'adjr2':
         model_select = np.argmax([model.rsquared_adj for model in best_models])
      else:
         print('Wrong criterion')

         
      return best_models[model_select]



