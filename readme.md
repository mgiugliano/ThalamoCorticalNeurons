# ThalamoCorticalNeurons

Simulating the biophysical and excitable behavior of long-range projection thalamocortical neurons, 
within the (https://www.flagera.eu/wp-content/uploads/2020/06/FLAG-ERA_JTC2019_HBP_NeuronsReunited.pdf)["Neurons reunited" FLAG-ERA JTC 2019 project]. This work has been cofunded by SISSA and FLAG-ERA (Joint Transnational Call 2019 - Human Brain Project - Project "Neurons reunited".

This repository is heavily based on a fork of (https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006753)[Iavarone et al. 2019] and the code released (https://senselab.med.yale.edu/ModelDB/showmodel.cshtml?model=251881&file=/IavaroneEtAl_PLOSCompBio2019/cNAD_ltb.hoc#tabs-2)[ModelDB, accession number 251881], first modified by Michele GIUGLIANO.


Coauthors: 
Prof. Dr. Michele GIUGLIANO (SISSA, Italy), 
Dr. Nestor TIMONIDIS (Radboud Univ., the Netherlands), 
Ludovica LIOTTI (SISSA, Italy)


Additional key contribution: 
Dr. Justas BIRGIOLAS (Ronin Institute, USA; author of BlenderNEURON)

```
.
├── cNAD_ltb_MG.hoc
├── mechanisms
│   ├── SK_E2.mod
│   ├── TC_HH.mod
│   ├── TC_ITGHK_Des98.mod
│   ├── TC_Ih_Bud97.mod
│   ├── TC_Nap_Et2.mod
│   ├── TC_cadecay.mod
│   ├── TC_iA.mod
│   └── TC_iL.mod
├── models
│   ├── TCbiophys.hoc
│   └── TCtemplate.hoc
└── morphologies
    └── EP23HI-LPLC_shrinkcorrect_splicedlayers_pictures23rotated_correctedlayers1.swc
```



## first_test.py

Starting code to instantiate one simulation, inject somatic current to elicit 1 AP, and then
plot the somatic, dendritic, and axonal responses as *.png figure files.


Launch it (interactively) as: 
```bash
nrnivmodl ./mechanisms/           # compiles all "mechanisms"
python3 -i first_test.py  # actual python script launch
```

Requires: 
```bash
pip3 install neuron matplotlib numpy
```

Tested successfully under: 
Python3 (3.9.12), NEURON (8.1.0), matplotlib (3.5.1), numpy (1.20.1)




## first_blender_test.py

First experiment to import into Blender the result of a simulation (as above).

First install:
    - the (https://blenderneuron.org)[BlenderNEURON python library and Blender add-on]
    - (the old version of) (https://download.blender.org/release/Blender2.79/)[Blender 2.79b]

Launch Blender.

Launch the python script (interactively) as: 
```bash
unset DISPLAY                     # required if "can't open DISPLAY" error
nrnivmodl ./mechanisms/           # compiles all "mechanisms"
python3 -i first_test_blender.py  # actual python script launch
/Applications/Blender/blender.app/Contents/MacOS/blender --python ./blender_script.py
```

- within Blender, click on the tab "BlenderNEURON"
- check that "Status" reads "Connected"



Tested successfully under: 
Python3 (3.9.12), NEURON (8.1.0), matplotlib (3.5.1), numpy (1.20.1), Blender (2.79b)

