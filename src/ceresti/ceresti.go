package main

import (
	"github.com/ant0ine/go-json-rest"
	"net/http"
)

type Task struct {
	taskid int64
	taskdesc string
	duedate string
	completed bool
}

func main() {
	handler := rest.ResourceHandler{
                EnableRelaxedContentType: true,
        }
	handler.SetRoutes(
		rest.Route{"POST", "/add", CreateTask},
		rest.Route{"GET", "/task/:id", ReadTask},
		rest.Route{"GET", "/task/list", ReadAllTasks},
		rest.Route{"POST", "/task/:id", UpdateTask},
		rest.Route{"POST", "/task/delete/:id", DeleteTask},
	)
	http.ListenAndServe(":8080", &handler)
}

var store = map[string]*Task{}

func ReadAllTasks(w *rest.ResponseWriter, r *rest.Request) {
        tasks := make([]*Task, len(store))
        i := 0
        for _, task := range store {
                tasks[i] = task
                i++
        }
        w.WriteJson(&tasks)
}

func CreateTask(w *rest.ResponseWriter, r *rest.Request) {
	task := Task{}
	err := r.DecodeJsonPayload(&task)
	if err != nil {
		rest.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	if task.taskdesc == "" {
		rest.Error(w, "Task Description required", 400)
		return
	}
	if task.duedate == "" {
		rest.Error(w, "Due Date required", 400)
		return
	}
	if task.completed == "" {
		rest.Error(w, "Completed required", 400)
		return
	}
	task.taskid = 1
	store[task.id] = &id
	w.WriteJson(&task)
}

