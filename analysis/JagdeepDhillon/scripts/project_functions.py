{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "256f21c5-a510-466a-8175-4fa5716bf273",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Here we are making a function which takes the process of our analysis pipeline, and makes it more simple to use.\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import numpy as np\n",
    "import os\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "\n",
    "def load_and_process(url_or_path_to_csv_file):\n",
    "       \n",
    "        #First method chain (dropping null values, renaming columns)\n",
    "        impacts1 = (pd.read_csv(url_or_path_to_csv_file)\n",
    "                .dropna()\n",
    "                .rename(columns={\"Period Start\": \"Risk Period Start\", \"Period End\": \"Risk Period End\", \"Object Name\": \"Asteroid Name\"})\n",
    "                .rename(columns={\"Asteroid Velocity\": \"Asteroid Velocity (km/s)\", \"Asteroid Magnitude\": \"Asteroid Magnitude (au)\"})\n",
    "    \n",
    "        )\n",
    "        #Second method chain (dropping columns, organizing data)\n",
    "        impacts2 = (impacts1.reset_index(drop=True)\n",
    "                .drop(['Maximum Torino Scale'], axis = 1)\n",
    "                .sort_values(by = 'Risk Period Start', ascending = True)\n",
    "        \n",
    "        \n",
    "        )\n",
    "        return impacts2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "364da07e-a897-4861-91e9-7ccc9868178f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
