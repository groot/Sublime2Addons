import sublime, sublime_plugin

class CollapseClassesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view

		i = 0
		while (i<view.size()):
			c = view.find('class|interface', i)
			if(c is None):
				#print "done folding"
				return

			p = 0		
			first = view.find('\{',c.b)
			i = first.b
			p = p + 1

			while (p>0):
				#print "p=",p,"i=",i
				left  = view.find('\{', i)
				right = view.find('\}', i)
				if(not left is None and left.b<right.b):
					p = p + 1
					i = left.b
				else:
					i = right.b
					p = p - 1

			#print "p= 0","i=",i,"folding"
			view.fold(sublime.Region(view.line(c).b, i))
