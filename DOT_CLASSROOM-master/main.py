import rpy2.robjects as robjects

def evaluate_r_code(r_code):
    try:
        # Evaluate the R code
        r = robjects.r(r_code)
        # Return the result as a string
        return (r[0])
    except Exception as e:
        # If there's an error, return the error message as a string
        return (e)

r_code = """
# Your R code goes here
result <- 2 + 9
result
"""

d=evaluate_r_code(r_code)
print(type(d))