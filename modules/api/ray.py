from ray import serve
import ray

from modules.api.raypi import Raypi

import time
import os


#ray.init(os.environ.get("RAY_HEAD_ADDRESS", ""))
#ray.init("ray://localhost:10001")
if "RAY_HEAD_ADDRESS" in os.environ:
    ray.init(os.environ.get("RAY_HEAD_ADDRESS"))
else:
    ray.init()

def ray_only():
    serve.shutdown()
    if "RAY_DOCKER" in os.environ:
        print("starting ray in docker")
        serve.start(
            detached=True, 
            http_options={
                        "host": os.environ.get("RAY_IP", "0.0.0.0"), 
                        "port": int(os.environ.get("RAY_PORT", 8000))
                        }
        )
    else:    
        serve.start(
            http_options={
                        "host": os.environ.get("RAY_IP", "0.0.0.0"), 
                        "port": int(os.environ.get("RAY_PORT", 8000))
                        }
        )
    print(f"Starting Raypi on port {os.environ.get('RAY_PORT', 8000)}")
    serve.run(Raypi.bind(), port=int(os.environ.get("RAY_PORT", 8000)), route_prefix="/sdapi/v1")  #route_prefix="/sdapi/v1" # Call the launch_ray method to get the FastAPI app
    print("Done setting up replicas! Now accepting requests...")
    while True:
        time.sleep(1000)
#import subprocess
#from ray import serve
#import ray
#from modules.api.raypi import Raypi
#import time
#import os

# Define the ray start command
#ray_start_command = "ray start --head --dashboard-host=0.0.0.0 --port=6379"

# Run the ray start command
#subprocess.Popen(ray_start_command, shell=True)

# Sleep briefly to allow the Ray cluster to start
#time.sleep(5)  # Adjust the sleep duration as needed

# Initialize Ray
#if "RAY_HEAD_ADDRESS" in os.environ:
 #   ray.init(os.environ.get("RAY_HEAD_ADDRESS"))
#else:
 #   ray.init()

#def ray_only():
 #   serve.shutdown()
  #  if "RAY_DOCKER" in os.environ:
   #     print("starting ray in docker")
    #    serve.start(
     #       detached=True, 
      #      http_options={
       #         "host": os.environ.get("RAY_IP", "0.0.0.0"), 
        #        "port": int(os.environ.get("RAY_PORT", 8000))
         #   }
        #)
    #else:    
     #   serve.start(
      #      http_options={
       #         "host": os.environ.get("RAY_IP", "0.0.0.0"), 
        #        "port": int(os.environ.get("RAY_PORT", 8000))
         #   }
        #)
    #print(f"Starting Raypi on port {os.environ.get('RAY_PORT', 8000)}")
    #serve.run(Raypi.bind(), port=int(os.environ.get("RAY_PORT", 8000)), route_prefix="/sdapi/v1")
    #print("Done setting up replicas! Now accepting requests...")
    #while True:
    #    time.sleep(1000)

#ray_only()
