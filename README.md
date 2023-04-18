# django-rest-apis
Make a very simple backend app in django/restapis: 
Take 3 django models: 1) Class (title and description field) 2) Lessons (title, description and resources_count) 3) Resources (title, description, resource_type). You can assume resource_type as video/pdf etc. 

Assume manytomany relationships between resources to lessons and also between lessons to class (same resource can be part of different lessons and same lesson can also be part of different classes) 

In your test dataset, you can add 1 class, 2-3 lessons and for each lesson - 3-4 resources as instances in the database so that you can generate valid json and properly check your database query efficiency before sharing the assignment.
 
Create a single api url and view which should return a single json for particular class basis its id (details of class, list of all lessons and their details under that class and also list and details of all resources grouped by their resource_type under each lesson). While returning the json, it should use a serialiser.

The url should also return a very basic django template (u can ignore css or beautification etc., just use html ) to render/display all the details of that json.
