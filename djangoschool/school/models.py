from django.db import models

class ExamScore(models.Model):

	allsubject = (('คณิตศาสตร์','คณิตศาสตร์'),
				  ('วิทยาศาสตร์','วิทยาศาสตร์'),
				  ('ศิลปะ','ศิลปะ'),
				  ('ภาษาอังกฤษ','ภาษาอังกฤษ'),
				  ('คอมพิวเตอร์','คอมพิวเตอร์'),
				  ('ดนตรี','ดนตรี'))

	subject = models.CharField(max_length=200, choices=allsubject, default='math')
	student_name = models.CharField(max_length=200)
	score = models.IntegerField(default=0) 

	def __str__(self):
		return self.student_name+' | '+"วิชา"+' '+self.subject+' | '+str(self.score)+' '+"คะแนน" 
