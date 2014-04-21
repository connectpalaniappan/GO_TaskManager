package main

import (
	"github.com/ant0ine/go-json-rest/rest"
	"net/http"
	"strconv"
)

var check bool = false
var val int64 = 0;

func main() {
	handler := rest.ResourceHandler{
                EnableRelaxedContentType: true,
        }
	handler.SetRoutes(
		&rest.Route{"POST", "/task/add", CreateTask},
		&rest.Route{"GET", "/task/list", ReadAllTasks},
		&rest.Route{"GET", "/task/:id", ReadTask},		
		&rest.Route{"POST", "/task/:id", UpdateTask},
		&rest.Route{"POST", "/task/delete/:id", DeleteTask},
	)
	http.ListenAndServe(":8080", &handler)
}

type Task struct {
	Id int64
	Desc string
	Due string
	Completed bool
}

func increment() int64{
    val = val + 1
	return val
}

var store = map[int64]*Task{}

func CreateTask(w rest.ResponseWriter, r *rest.Request) {
	task := Task{}
	err := r.DecodeJsonPayload(&task)
	if err != nil {
		rest.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	if task.Desc == "" {
		rest.Error(w, "Task Description required", 400)
		return
	}
	if task.Due == "" {
		rest.Error(w, "Due Date required", 400)
		return
	}
	task.Id = increment()
	store[task.Id] = &task
	w.WriteJson(&task)
}

func ReadTask(w rest.ResponseWriter, r *rest.Request) {
	Id, _ := strconv.ParseInt(r.PathParam("id"),0,64)
	task := store[Id]
	if task == nil {
		rest.NotFound(w, r)
		return
	}
	w.WriteJson(&task)
}

func ReadAllTasks(w rest.ResponseWriter, r *rest.Request) {
        tasks := make([]*Task, len(store))
        i := 0
        for _, task := range store {
                tasks[i] = task
                i++
        }
        w.WriteJson(&tasks)
}

func UpdateTask(w rest.ResponseWriter, r *rest.Request) {
	newtask := Task{}
	err := r.DecodeJsonPayload(&newtask)
	if err != nil {
		rest.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	Id, _ := strconv.ParseInt(r.PathParam("id"),0,64)
	oldtask := store[Id]
	if oldtask == nil {
		rest.NotFound(w, r)
		return
	}
	if newtask.Desc != "" {
		oldtask.Desc = newtask.Desc
	}
	if newtask.Due != "" {
		oldtask.Due = newtask.Due
	}
	if newtask.Completed == true || newtask.Completed == false {
		oldtask.Completed = newtask.Completed
	}
	store[Id] = oldtask
	w.WriteJson(&oldtask)
}

func DeleteTask(w rest.ResponseWriter, r *rest.Request) {
	Id, _ := strconv.ParseInt(r.PathParam("id"),0,64)
	delete(store,Id)
}



