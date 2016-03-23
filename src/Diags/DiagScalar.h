#ifndef DIAGSCALAR_H
#define DIAGSCALAR_H

#include "Diag.h"

#include "Params.h"
#include "Patch.h"
#include "SmileiMPI.h"


class DiagScalar : public Diag {
    friend class SmileiMPI;

public :

    DiagScalar( Params &params, SmileiMPI* smpi, Patch* patch, int diagId );
    DiagScalar() {};
    ~DiagScalar();

    virtual void openFile( Params& params, SmileiMPI* smpi, VectorPatch& vecPatches, bool newfile );
    virtual void setFile( Diag* diag );

    virtual void closeFile();

    virtual void prepare( Patch* patch, int timestep );

    virtual void run( Patch* patch, int timestep );

    virtual void write(int timestep);

    //! get a particular scalar
    double getScalar(std::string name);

    // Reset stored values
    void reset( int timestep ) {
	 if (  timeSelection->theTimeIsNow(timestep) &&  timeSelection->inProgress(timestep) )
	     for (int iscalar=0 ; iscalar<out_value.size() ; iscalar++)
		 out_value[iscalar] = 0.;
    }

private :

    // Specific methods
    void compute( Patch* patch, int timestep );


    //! set a particular scalar
    void setScalar(std::string name, double value);

    //! increment a particular scalar
    void incrementScalar(std::string name, double value);

    //! append to outlist
    void append(std::string, double);

    //! prepend to outlist
    void prepend(std::string, double);

    //! check if key is allowed
    bool allowedKey(std::string);

    bool defined(std::string);

    //! write precision
    unsigned int precision;

    //! list of keys for scalars to be written
    std::vector<std::string> vars;

    //! these are lists to keep variable names and values
    std::vector<std::string> out_key;
    std::vector<double>      out_value;
    //! width of each field
    std::vector<unsigned int> out_width;

    //! copied from params
    double cell_volume;

    //! this is copied from params
    double res_time;
    
    double dt;

    //! output stream
    std::ofstream fout;

    //! initial energy (kinetic + EM)
    double Energy_time_zero;
    
    //! energy used for the normalization of energy balance (former total energy)
    double EnergyUsedForNorm;



};

#endif

