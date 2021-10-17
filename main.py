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
API_KEY = os.getenv("TEST_BXSA_API")
IN_FILE = '/media/sf_LouxBox/ListeReminders.txt'
CATEGORY = 'PPN_DELETED'




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
    response, reminders = api.get_reminder_id(mmsid[0:18],CATEGORY)
    if response == "Error" :
        continue
    for reminder_id in reminders :
        reponse = api.delete_reminder(mmsid,reminder_id)
    logger.debug("{}::{}::{}".format(mmsid[0:18],reminder_id,reponse))
# code_list=[]
# for row in table['row']:
#     code_list.append(row['code'])
# logger.debug(len(code_list))
# # On vachercher tous les codes assiciés à des lecteurs actifs dans Alma 
# # Rapport 	/shared/Bordeaux NZ 33PUDB_NETWORK/prod/SCOOP/Utilisateurs/Liste des codes statistiques/Codes stat
# # IsFinished
# isFinished = 'false'
# token = ''
# cpteur = 0
# while isFinished == 'false' :
#     status, code_stats = api.get_stat(path_to_report,limit=25,token=token)
#     # logger.debug(code_stats)
#     reponsexml = ET.fromstring(code_stats)
#     if reponsexml.findall(".//QueryResult/ResumptionToken") :
#         token=reponsexml.find(".//QueryResult/ResumptionToken").text
#     isFinished=reponsexml.find(".//QueryResult/IsFinished").text
#     logger.debug(token)
#     logger.debug(isFinished)
#     rows = reponsexml.findall(".//QueryResult/ResultXml/xmlns:rowset/xmlns:Row",ns)
    
#     for row in rows :
#         code = row.find("./xmlns:Column1",ns).text
#         exemple = row.find("./xmlns:Column2",ns).text
#         if code not in code_list :
#             cpteur = cpteur + 1
#             logger.info("{}::{}".format(code,exemple))
# logger.info(cpteur)
    