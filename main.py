#!/usr/bin/python3
# -*- coding: utf-8 -*-
# from Alma_Apis_Interface import 
import json
import os
import AlmaApi
from datetime import date, timedelta
import logging
import logs


SERVICE = 'Alma_Delete_Reminders'
API_KEY = os.getenv("PROD_NETWORK_BIB_API")
IN_FILE = '/media/sf_LouxBox/ListeReminders.txt'




#On initialise le logger
logs.init_logs(os.getenv('LOGS_PATH'),SERVICE,'DEBUG')
logger = logging.getLogger(SERVICE)
#On récupère la liste des mmsid à traiter
f = open(IN_FILE, "rU")
for line in f:
    mmsid = line.strip()
    logger.debug(mmsid)
    if mmsid[0:1] != '9':
        logger.error("{} n'est pas un mmsid".format(mmsid))
        continue
    #On obtient la liste des identifiants des reminders liés à la notice
    api = AlmaApi.AlmaRecords(API_KEY,'EU',SERVICE)
    response, reminders = api.get_reminder_id(mmsid[0:18])
    if response == "Error" :
        continue
    for reminder_id in reminders :
        reponse = api.delete_reminder(mmsid,reminder_id)
    logger.debug("{}::{}::{}".format(mmsid[0:18],reminder_id,reponse))

    