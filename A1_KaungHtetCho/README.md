# A1 Assignment Report and Usage  

**Name:** Kaung Htet Cho  
**Student ID:** st124092  

## Task 1: Python Notebook for Experiments and Model Training  
The work for Task 1 is documented in the following file:  
**`A1_KaungHtetCho/notebooks/A1_Predicting_Car_Price.ipynb`**  

## Task 2: Analysis and Report on Model and Dataset  
All analysis, discussions, and insights are included within the notebook mentioned above.  

## Task 3: Deployment Webpage  
For this task, I implemented two Docker configurations to support both development and production environments:  

- **`docker/Dockerfile`**: A multi-stage Dockerfile that supports both development and production builds.  
  - **Development environment**: Allows experimentation and testing with direct access to the local machine as a superuser.  
  - **Production environment**: Provides a lightweight, minimal library setup optimized for running the application.  

## Usage Instructions  

### Notes  
For the assignment, only the **production environment** is relevant. The development setup is provided solely for testing purposes and does not need to be executed.  

### Steps to Build and Run  

Clone the repository first **https://github.com/KaungHtetCho-22/ML-Assignments.git** 

1. **How to build the production Docker image:**  
```bash
  sh A1_KaungHtetCho/scripts/build_prod_img.sh
```
**Note: The image is already on Docker Hub - you can simply pull and run it, though build instructions are included in the compose file as a backup option.**

Please login to docker hub, and use the following command to pull the image.
```bash 
docker pull koala007/a1_assignment:prod
```

2. **Run the Production Container** 
#### To run in detached mode:  
To build from the start using this:
  ```bash
  docker-compose -f A1_KaungHtetCho/docker/docker-compose.prod.yml up -d --build
  ```
Access the webpage by navigating to http://localhost:8000 in your browser

To use pre-pushed image from docker hub, uncomment     # image: koala007/a1_assignment:prod in docker-compose and run with:
  ```bash
  docker-compose -f A1_KaungHtetCho/docker/docker-compose.prod.yml up -d
  ```



#### Development Setup (Optional for Testing and not intended for assignment submission)
1. **Build the development Docker image:**  
   ```bash
   sh A1_KaungHtetCho/scripts/build_devel_img.sh
    ```
2. **Run the development Container** 
#### To run in detached mode:  
```bash
docker-compose -f A1_KaungHtetCho/docker/docker-compose.devel.yml up -d
```