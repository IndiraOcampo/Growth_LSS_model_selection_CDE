import sys
import numpy as np
from classy import Class
#import matplotlib.pyplot as plt
import pandas as pd
import csv

#zbins
zs = np.linspace(0.1, 2.0, 10)
#############################################################################################################
#TRAINING
#############################################################################################################
# LCDM parameters
ntr = 2500 #training data size (times 2, because ntr·LCDM + ntr·CDE)
omega_cdm = np.linspace(0.01,0.7,ntr)

#CDE parameters
beta_bin = 1
nn = 50
betas = np.linspace(0.001,0.5,nn)
omega_cde = np.linspace(0.01,0.7,nn)

#Percent error
perc_err = 0.02

header = ['fs8_1', 'sfs8_1']
for i in range(2,len(zs)+1):
    header.append('fs8_%d'%i)
    header.append('sfs8_%d'%i)
header.append('target')

print('creating the training data')

with open('./Training_beta%d.csv' %beta_bin, 'w') as f:
    writer = csv.writer(f, delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(header)
    #LCDM cases
    for omega_cdm in omega_cdm:
        cosmo = Class()
        common_settings = {# LambdaCDM parameters
                           'kappa':0.621,
                           'omega_b':0.02225,
                           'omega_cdm_tilde':omega_cdm,
                           'ln10^{10}A_s':3.044,
                           'n_s': 0.9660499,
                           'tau_reio': 0.0522,
            
                           'beta_1' : 0.00000001,
                           'beta_2' : 0.00000001,
                           'beta_3' : 0.00000001,
                           'Omega_Lambda': 0,
                           'Omega_fld': 0,
                           'Omega_scf': -1,
                           'phi_ini_scf':0.00000001,
                           'phi_prime_ini_scf':0.0000001,
                           # output and precision parameters
                           'output':'mPk dTk',
                           'P_k_max_h/Mpc':1.0,
                           'z_pk': ', '.join(str(z) for z in zs)
                           }
        
        M = Class()
        M.set(common_settings)
        M.compute()
        
        h0 = M.h()
        fsigma8 = np.asarray([M.scale_independent_growth_factor_f(z_val)*M.sigma(8./h0,z_val) for z_val in zs])
        err_fsigma8 = perc_err*fsigma8
        cij = np.diagflat(err_fsigma8*err_fsigma8)
        np.random.seed(314159)
        fsigma8_noisy = np.random.multivariate_normal(fsigma8, cij, 1)
        fsigma8_w_err = np.column_stack((fsigma8_noisy[0], err_fsigma8)).ravel()
        writer.writerow(np.append(fsigma8_w_err,0))
        M.struct_cleanup()
        M.empty()

    #CDE cases
    for omega_cdm in omega_cde:
        for beta in betas:
            cosmo = Class()
            common_settings = {# LambdaCDM parameters
                               'kappa':0.621,
                               'omega_b':0.02225,
                               'omega_cdm_tilde':omega_cdm,
                               'ln10^{10}A_s':3.044,
                               'n_s': 0.9660499,
                               'tau_reio': 0.0522,
                
                               'beta_1': beta,  #Varying only beta_1
                               'beta_2' : 0.00000001,
                               'beta_3' : 0.00000001,
                               'Omega_Lambda': 0,
                               'Omega_fld': 0,
                               'Omega_scf': -1,
                               'phi_ini_scf':0.00000001,
                               'phi_prime_ini_scf':0.0000001,
                               'output':'mPk dTk',
                               'P_k_max_h/Mpc':1.0,
                               'z_pk': ', '.join(str(z) for z in zs)
                               }
            
            M = Class()
            M.set(common_settings)
            M.compute()
            
            h0 = M.h()
            fsigma8 = np.asarray([M.scale_independent_growth_factor_f(z_val)*M.sigma(8./h0,z_val) for z_val in zs])
            err_fsigma8 = perc_err*fsigma8
            cij = np.diagflat(err_fsigma8*err_fsigma8)
            np.random.seed(314159)
            fsigma8_noisy = np.random.multivariate_normal(fsigma8, cij, 1)
            fsigma8_w_err = np.column_stack((fsigma8_noisy[0], err_fsigma8)).ravel()
            writer.writerow(np.append(fsigma8_w_err,1))
            M.struct_cleanup()
            M.empty()
f.close() 

print('creating the test data')

#############################################################################################################
#TEST
#############################################################################################################
np.random.seed(314159)
# LCDM parameters
nte = 750 #training data size (times 2, because ntr·LCDM + ntr·CDE)
omega_cdm = np.random.uniform(0.01,0.7,nte)

#CDE parameters
nnte = 30
omega_cde = np.random.uniform(0.01,0.7,nnte)
betas = np.random.uniform(0.001,0.5,25)

with open('./Test_beta%d.csv' %beta_bin, 'w') as f:
    writer = csv.writer(f, delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(header)
    #LCDM cases
    for omega_cdm in omega_cdm:
        cosmo = Class()
        common_settings = {# LambdaCDM parameters
                           'kappa':0.621,
                           'omega_b':0.02225,
                           'omega_cdm_tilde':omega_cdm,
                           'ln10^{10}A_s':3.044,
                           'n_s': 0.9660499,
                           'tau_reio': 0.0522,
            
                           'beta_1' : 0.00000001,
                           'beta_2' : 0.00000001,
                           'beta_3' : 0.00000001,
                           'Omega_Lambda': 0,
                           'Omega_fld': 0,
                           'Omega_scf': -1,
                           'phi_ini_scf':0.00000001,
                           'phi_prime_ini_scf':0.0000001,
                           'output':'mPk dTk',
                           'P_k_max_h/Mpc':1.0,
                           'z_pk': ', '.join(str(z) for z in zs)
                           }
        
        M = Class()
        M.set(common_settings)
        M.compute()
        
        h0 = M.h()
        fsigma8 = np.asarray([M.scale_independent_growth_factor_f(z_val)*M.sigma(8./h0,z_val) for z_val in zs])
        err_fsigma8 = perc_err*fsigma8
        cij = np.diagflat(err_fsigma8*err_fsigma8)
        np.random.seed(314159)
        fsigma8_noisy = np.random.multivariate_normal(fsigma8, cij, 1)
        fsigma8_w_err = np.column_stack((fsigma8_noisy[0], err_fsigma8)).ravel()
        writer.writerow(np.append(fsigma8_w_err,0))
        M.struct_cleanup()
        M.empty()

    #CDE cases
    for omega_cdm in omega_cde:
        for beta in betas:
            cosmo = Class()
            common_settings = {# LambdaCDM parameters
                               'kappa':0.621,
                               'omega_b':0.02225,
                               'omega_cdm_tilde':omega_cdm,
                               'ln10^{10}A_s':3.044,
                               'n_s': 0.9660499,
                               'tau_reio': 0.0522,
                               'beta_1': beta,  #Varying only beta_1
                               'beta_2' : 0.00000001,
                               'beta_3' : 0.00000001,
                               'Omega_Lambda': 0,
                               'Omega_fld': 0,
                               'Omega_scf': -1,
                               'phi_ini_scf':0.00000001,
                               'phi_prime_ini_scf':0.0000001,
                               'output':'mPk dTk',
                               'P_k_max_h/Mpc':1.0,
                               'z_pk': ', '.join(str(z) for z in zs)
                               }
            
            M = Class()
            M.set(common_settings)
            M.compute()
            
            h0 = M.h()
            fsigma8 = np.asarray([M.scale_independent_growth_factor_f(z_val)*M.sigma(8./h0,z_val) for z_val in zs])
            err_fsigma8 = perc_err*fsigma8
            cij = np.diagflat(err_fsigma8*err_fsigma8)
            np.random.seed(314159)
            fsigma8_noisy = np.random.multivariate_normal(fsigma8, cij, 1)
            fsigma8_w_err = np.column_stack((fsigma8_noisy[0], err_fsigma8)).ravel()
            writer.writerow(np.append(fsigma8_w_err,1))
            M.struct_cleanup()
        M.empty()
f.close() 

exit() 
