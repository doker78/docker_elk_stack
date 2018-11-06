from django.db import models

OS_OPTIONS = [
	('Ubuntu-Desktop', 'Ubuntu-Desktop'),
	('Ubuntu-Server', 'Ubuntu-Server'),
]
class Vm(models.Model):
	vm_name = models.CharField("Virtual Mashine Name", max_length=100, blank=False,
null=False, unique=True)
	number_of_cpu = models.IntegerField(default=2, blank=False, null=False)
	memory_size = models.IntegerField(default=1024, blank=False, null=False)
	OS = models.CharField(max_length=100, choices=OS_OPTIONS, default='Ubuntu-Desktop', blank=False, null=False)
	vswitch_name = models.CharField(max_length=100, default="vSwitch0")
	prof_profile_name = models.CharField(max_length=100, default="VM network")
	vlan_id = models.IntegerField(default="1")