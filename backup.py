import os
import time

# Backup commands
backup_commands = [
    "docker exec -it clab-naas_gw_stitching-AGG1 cat /xr-storage/config/config/running/alternate_cfg/router.cfg > /home/ubuntu/naas/naas_gw_stitching/config/AGG1.cfg",
    "docker exec -it clab-naas_gw_stitching-AGG2 cat /xr-storage/config/config/running/alternate_cfg/router.cfg > /home/ubuntu/naas/naas_gw_stitching/configAGG2.cfg",
    "docker exec -it clab-naas_gw_stitching-AL1 cat /xr-storage/config/config/running/alternate_cfg/router.cfg > /home/ubuntu/naas/naas_gw_stitching/config/AL1.cfg",
    "docker exec -it clab-naas_gw_stitching-AL2 cat /xr-storage/config/config/running/alternate_cfg/router.cfg > /home/ubuntu/naas/naas_gw_stitching/config/AL2.cfg",
    "docker exec -it clab-naas_gw_stitching-BX cat /xr-storage/config/config/running/alternate_cfg/router.cfg > /home/ubuntu/naas/naas_gw_stitching/config/BX.cfg",
    "docker exec -it clab-naas_gw_stitching-CPE1 cat /xr-storage/config/config/running/alternate_cfg/router.cfg > /home/ubuntu/naas/naas_gw_stitching/config/CPE1.cfg",
    "docker exec -it clab-naas_gw_stitching-CPE2 cat /xr-storage/config/config/running/alternate_cfg/router.cfg > /home/ubuntu/naas/naas_gw_stitching/config/CPE2.cfg",
    "docker exec -it clab-naas_gw_stitching-DR cat /xr-storage/config/config/running/alternate_cfg/router.cfg > /home/ubuntu/naas/naas_gw_stitching/config/DR.cfg",
    "docker exec -it clab-naas_gw_stitching-GW cat /xr-storage/config/config/running/alternate_cfg/router.cfg > /home/ubuntu/naas/naas_gw_stitching/config/GW.cfg",
    "docker exec -it clab-naas_gw_stitching-OLT cat /xr-storage/config/config/running/alternate_cfg/router.cfg > /home/ubuntu/naas/naas_gw_stitching/config/OLT.cfg",
    "docker exec -it clab-naas_gw_stitching-P1 cat /xr-storage/config/config/running/alternate_cfg/router.cfg > /home/ubuntu/naas/naas_gw_stitching/config/P1.cfg",
    "docker exec -it clab-naas_gw_stitching-P1L cat /xr-storage/config/config/running/alternate_cfg/router.cfg > /home/ubuntu/naas/naas_gw_stitching/config/P1L.cfg",
    "docker exec -it clab-naas_gw_stitching-P2 cat /xr-storage/config/config/running/alternate_cfg/router.cfg > /home/ubuntu/naas/naas_gw_stitching/config/P2.cfg",
    "docker exec -it clab-naas_gw_stitching-P2L cat /xr-storage/config/config/running/alternate_cfg/router.cfg > /home/ubuntu/naas/naas_gw_stitching/config/P2L.cfg",
    "docker exec -it clab-naas_gw_stitching-RS cat /xr-storage/config/config/running/alternate_cfg/router.cfg > /home/ubuntu/naas/naas_gw_stitching/config/RS.cfg",
    "docker exec -it clab-naas_gw_stitching-eREF cat /xr-storage/config/config/running/alternate_cfg/router.cfg > /home/ubuntu/naas/naas_gw_stitching/config/eREF.cfg",
    "docker exec -it clab-naas_gw_stitching-iRR4 cat /xr-storage/config/config/running/alternate_cfg/router.cfg > /home/ubuntu/naas/naas_gw_stitching/config/iRR4.cfg",
    "docker exec -it clab-naas_gw_stitching-iRR6 cat /xr-storage/config/config/running/alternate_cfg/router.cfg > /home/ubuntu/naas/naas_gw_stitching/config/iRR6.cfg"
]

# Execute backup commands
for command in backup_commands:
    os.system(command)
    time.sleep(1)

print("Backup completed.")
