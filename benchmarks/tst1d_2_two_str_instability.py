# ----------------------------------------------------------------------------------------
# 					SIMULATION PARAMETERS FOR THE PIC-CODE SMILEI
# ----------------------------------------------------------------------------------------

import math
L  = 1.12			# wavelength=simulation box length
dn = 0.001			# amplitude of the perturbation


Main(
    geometry = "1d3v",
     
    interpolation_order = 2,
     
    cell_length = [0.01],
    sim_length  = [L],
    
    number_of_patches = [ 16 ],
    
    timestep = 0.0095,
    sim_time = 50.,
     
    EM_boundary_conditions = [ ['periodic'] ],
     
    random_seed = 0
)


Species(
	name = "ion",
	position_initialization = "regular",
	momentum_initialization = "cold",
	n_part_per_cell = 10,
	mass = 1836.0,
	charge = 1.0,
	nb_density = 1.,
	#time_frozen = 10000.0,
	boundary_conditions = [
		["periodic", "periodic"],
	],
	time_frozen = 0.1
)
Species(
	name = "eon1",
	position_initialization = "regular",
	momentum_initialization = "cold",
	n_part_per_cell = 10,
	mass = 1.0,
	charge = -1.0,
	nb_density = cosine(0.5,xamplitude=dn,xlength=L, xnumber=1),
	mean_velocity = [-0.1,0.0,0.0],
	boundary_conditions = [
		["periodic", "periodic"],
	],
)
Species(
	name = "eon2",
	position_initialization = "regular",
	momentum_initialization = "cold",
	n_part_per_cell = 10,
	mass = 1.0,
	charge = -1.0,
	nb_density = cosine(0.5,xamplitude=dn,xlength=L, xnumber=1),
	mean_velocity = [0.1,0.0,0.0],
	boundary_conditions = [
		["periodic", "periodic"],
	],
)


every = 100

DiagScalar(
    every = every,
)	

DiagFields(
    every = every,
    fields = ['Ex','Ey','Ez','By_m','Bz_m','Rho']
)

DiagParticleBinning(
	output = "density",
	every = every,
	species = ["eon1","eon2"],
	axes = [
		["x", 0., L, 50],
		["px", -0.4, 0.4, 100]
	]
)

DiagTrackParticles(
	species = "ion", 
	every = 1000,
	filter = lambda x, px, py, pz: (x<0.02), 
)
