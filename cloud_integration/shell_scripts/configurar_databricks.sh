#!/bin/bash

# Variables
DATABRICKS_HOST="https://adb-3008024532543814.14.azuredatabricks.net"
DATABRICKS_TOKEN=$(cat credenciales.txt)

# Configuración
databricks configure --host $DATABRICKS_HOST --token <<< "$DATABRICKS_TOKEN"
