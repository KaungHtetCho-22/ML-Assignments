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

1. **Build the production Docker image:**  
   ```bash
   sudo sh A1_KaungHtetCho/build_prod_img.sh
    ```
2. **Run the Production Container** 
#### To run in detached mode:  
```bash
docker-compose -f A1_KaungHtetCho/docker/docker-compose.prod.yml up -d
```
Access the webpage by navigating to http://localhost:8000 in your browser.

#### To run in attached mode (view logs and output in the terminal):
```bash
docker-compose -f A1_KaungHtetCho/docker/docker-compose.prod.yml up
```

#### Development Setup (Optional for Testing and not intended for assignment submission)
1. **Build the development Docker image:**  
   ```bash
   sudo sh A1_KaungHtetCho/build_devel_img.sh
    ```
2. **Run the development Container** 
#### To run in detached mode:  
```bash
docker-compose -f A1_KaungHtetCho/docker/docker-compose.devel.yml up -d
```