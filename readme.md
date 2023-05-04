

# Run

1. Build a docker image using the dockerfile provided.

   ``sudo docker pull hzw77/colight:v0.1``

2. Pull the codes for CoLight.
``git clone https://github.com/Isabella156/Traffic-Signal-Control.git``


3. Run the built docker image to initiate a docker container. Please remember to mount the code directory.

   ``sudo docker run -it -v /path/to/your/workspace/colight/:/colight/ --shm-size=8gb --name hua_colight hzw77/colight:v0.1 /bin/bash``

​				``cd colight``

​				``python -O runexp.py``

​				Here, ``-O`` option cannot be omitted unless debug is necessary. In the file ``runexp.py``, the args can be changed.

* ``runexp.py``

  Run the pipeline under different traffic flows. Specific traffic flow files as well as basic configuration can be assigned in this file. For details about config, please turn to ``config.py``.

# Dataset

* Virtual Data

  Traffic file and road networks can be found in `data` folder, there are three types of virtual data, in `template_s`, `template_ls`, `template_lsr`

* Real Data

  Traffic file and road networks can be found in `data/NewYork`, `data/Jinan`, `data/Hangzhou`

# File

``agent.py``

An abstract class of different agents.

``CoLight_agent.py``

Proposed agent

``config.py``

 Configuration file of this project. 

``pipeline.py``

The whole pipeline is implemented in this module:

Start a simulator environment, run a simulation for certain time(one round), construct samples from raw log data, update the model and model pooling.

``generator.py``

A generator to load a model, start a simulator enviroment, conduct a simulation and log the results.

``anon_env.py``

Define a simulator environment to interact with the simulator and obtain needed data like features.

``construct_sample.py``

Construct training samples from original data. Select desired state features in the config and compute the corrsponding average/instant reward with specific measure time.

``updater.py``

Define a class of updater for model updating.
"# Traffic-Signal-Control" 
