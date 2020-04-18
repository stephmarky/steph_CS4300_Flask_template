from . import *  
from app.irsystem.models.helpers import *
from app.irsystem.models.helpers import NumpyEncoder as NumpyEncoder

project_name = "Stephanie's Cool Project Template"
net_id = "Stephanie Mark: srm276"

# EXAMPLE list to display
testlist = [["coffee", "bob", "hi"], ["myths", "anne", "moe"]]


@irsystem.route('/', methods=['GET'])
def search():
	query = request.args.get('search')
	if not query:
		data = []
		output_message = ''
	else:
		output_message = "Your search: " + query
		data = range(5)
	return render_template('search.html', name=project_name, netid=net_id, output_message=output_message, data=data, testlist=testlist)



