DATA_API (needs a better name) is developed as part of a personal Internet of Things (IoT) project. Its primary function is to facilitate a CRUD (Create, Read, Update, Delete) application interface for an Arduino/ESP-based device equipped with temperature and humidity sensors. This interface is designed to collect sensor data and store it directly on a local host machine, specifically a Raspberry Pi.

The Raspberry Pi is programmed to run a cron job script daily. This script's purpose is to gather the data collected from the previous day and upload it to an Amazon S3 bucket for storage.

This setup serves as a proof of concept for a personal IoT data management pipeline. The initial stages of data collection and storage demonstrate the project's viability. Future operations and more complex data processing tasks will be carried out within the AWS cloud environment, building on this foundational work.
