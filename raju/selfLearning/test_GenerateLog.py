from raju.utlites import Generatorlog

logger= Generatorlog.generate_logs()
logger.info(" Log started")

for i in range(1,7):
    logger.info(" the value of i is "+str(i))

logger.info(" Log completed")
