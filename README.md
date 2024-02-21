# DATA_API

This API is used for my personal IoT project.  It offers a simple crud application that receives requests from an Arduino/ESP device with temp/humidity sensor data.  This data is stored locally on the host machine (Raspberry Pi) which runs a cron job script for grabbing the previous day's data and pushing it up an S3 bucket.

This project is a proof of concept for a personal IoT data pipeline. The remainder of the operations will be implemented in AWS.