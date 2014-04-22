GO_TaskManager
==============

TaskManager using GO Technology



Developed in window 8
_______________________________________________

Required Technologies:
Go --> to run the source code
Python --> to run the test cases
_______________________________________________
Instruction to run the source code manually
1) set your GOPATH to point to directory which contains 'src' and 'test' 
2) Run the command in the terminal : go get -d github.com/ant0ine/go-json-rest/rest
3) Traverse to the directory %GOPATH%/src/ceresti
4) Run the command in the terminal : go run ceresti.go
5) In another terminal, traverse to the 'test' directory
	a) Adding data.json : curl --silent -H "Content-Type: application/json" --data @data.json  http://localhost:8080/task/add
	b) Adding data1.json : curl --silent -H "Content-Type: application/json" --data @data1.json  http://localhost:8080/task/add
	c) Adding data2.json : curl --silent -H "Content-Type: application/json" --data @data2.json  http://localhost:8080/task/add
	d) Adding data3.json : curl --silent -H "Content-Type: application/json" --data @data3.json  http://localhost:8080/task/add
	e) Adding data4.json : curl --silent -H "Content-Type: application/json" --data @data4.json  http://localhost:8080/task/add
	f) List 1 : curl --silent -H "Content-Type: application/json" http://localhost:8080/task/1
	g) List all : curl --silent -H "Content-Type: application/json" http://localhost:8080/task/list
	h) Update 2 : curl --silent -H "Content-Type: application/json" --data @data4.json  http://localhost:8080/task/2
	i) Delete 1 : curl --silent -H "Content-Type: application/json" --data @data4.json  http://localhost:8080/task/delete/1

______________________________________________
Instruction to run via the test scripts
1) set your GOPATH to point to directory which contains 'src' and 'test' 
2) Run the command in the terminal : go get -d github.com/ant0ine/go-json-rest/rest
3) Traverse to the directory %GOPATH%/src/ceresti
4) Run the command in the terminal : go run ceresti.go
5) In another terminal, traverse to the 'test' directory
6) Run the command : python compare_json.py	
7) All the test cases results and files compared will be listed out.
_______________________________________________
References and thanks to Antoine Imbert for http://ant0ine.github.io/go-json-rest/
My sincere thanks to ceresti for creating this opportunity.