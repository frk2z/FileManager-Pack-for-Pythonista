from objc_util import *
import os
import console

def main():
	UIApplication = ObjCClass('UIApplication')
	UIBarButtonItem = ObjCClass('UIBarButtonItem')
	rootVC = UIApplication.sharedApplication().keyWindow().rootViewController()
	tabVC = rootVC.detailViewController()
	
	methods = [fileExplorerButtonPressed]
	fileExplorerItemController = create_objc_class('fileExplorerItemController', NSObject, methods = methods)
	
	fileExplorerItemController = fileExplorerItemController.new()
	
	try:
		fileExplorerBarButtonItem = ObjCClass('fileExplorerBarButtonItem')
	except ValueError:
		fileExplorerBarButtonItem = create_objc_class('fileExplorerBarButtonItem', UIBarButtonItem)
	
	fileExplorerItem = fileExplorerBarButtonItem.alloc().initWithImage_style_target_action_(ns(ui.Image.named('iob:ios7_folder_outline_256')), 0, fileExplorerItemController, sel('fileExplorerButtonPressed'))
	fileExplorerItemController.fileExplorerItem = fileExplorerItem
	
	leftBarButtonItems = list(tabVC.persistentLeftBarButtonItems())
	leftBarButtonItems.append(fileExplorerItem)
	tabVC.persistentLeftBarButtonItems = ns(leftBarButtonItems)
	tabVC.reloadBarButtonItemsForSelectedTab()

def fileExplorerButtonPressed(_self, _cmd):
	path = console.input_alert('File Explorer')
	try:
		files = os.listdir(path)
		sfiles = "\n".join(files)
		console.alert(path, sfiles)
	except OSError:
		console.alert('Error', 'Path not found')

if __name__ == '__main__':
	main()