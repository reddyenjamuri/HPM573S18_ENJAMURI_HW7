SIM_POP_SIZE = 1000      # population size of simulated cohorts
TIME_STEPS = 1000        # length of simulation
ALPHA = 0.05             # significance level for calculating confidence intervals
NUM_SIM_COHORTS = 500    # number of simulated cohorts used to calculate prediction intervals

# details of a clinical study estimating the 5-year survival probability
OBS_N = 573             # number of patients involved in the study
OBS_5YEAR_ALIVE = 400   # number of participants survived beyond 5 years

# how to sample the posterior distribution of annual mortality probability
# minimum, maximum and the number of samples for the annual mortality probability
POST_L, POST_U, POST_N = 0.05, 0.25, 1000

