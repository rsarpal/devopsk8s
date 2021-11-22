import Vue from 'vue'
import VueRouter from 'vue-router'

// import components
import AllToDo from '@/components/AllToDo'

//Register the Vue Router plugin:
Vue.use(VueRouter)

// Add Routes
const routes = [
    { path: '/todos', component: AllToDo },
  ]


//Create a new instance of VueRouter and export it from the router.js module so other modules can use it
const router = new VueRouter({
    routes: routes,
    mode: 'history',
})
export default router