from objc_util import *
import console

def main():
	UIApplication = ObjCClass('UIApplication')
	UIBarButtonItem = ObjCClass('UIBarButtonItem')
	rootVC = UIApplication.sharedApplication().keyWindow().rootViewController()
	tabVC = rootVC.detailViewController()
	
	methods = [fileManagerButtonPressed]
	fileManagerItemController = create_objc_class('fileManagerItemController', NSObject, methods = methods)
	
	fileManagerItemController = fileManagerItemController.new()
	
	try:
		fileManagerBarButtonItem = ObjCClass('fileManagerBarButtonItem')
	except ValueError:
		fileManagerBarButtonItem = create_objc_class('fileManagerBarButtonItem', UIBarButtonItem)
	
	fileManagerItem = fileManagerBarButtonItem.alloc().initWithImage_style_target_action_(ns(ui.Image.named('iob:ios7_glasses_outline_256')), 0, fileManagerItemController, sel('fileManagerButtonPressed'))
	fileManagerItemController.fileManagerItem = fileManagerItem
	
	leftBarButtonItems = list(tabVC.persistentLeftBarButtonItems())
	leftBarButtonItems.append(fileManagerItem)
	tabVC.persistentLeftBarButtonItems = ns(leftBarButtonItems)
	tabVC.reloadBarButtonItemsForSelectedTab()

def fileManagerButtonPressed(_self, _cmd):
	path = console.input_alert('File Reader')
	try:
		file = open(path, 'r')
		console.alert(path, file.read())
		file.close()
		#console.quicklook(path)
	except IOError:
		console.alert('Error', 'Path not found')

if __name__ == '__main__':
		main()