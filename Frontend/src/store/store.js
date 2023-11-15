import { createStore } from 'vuex';
import axios from 'axios';

const store =  createStore({
  state: {
    access: '',
    refresh: '',
    idstudent: '',
    namestudent: ''
  },

  mutations: {
    
    initializeStore(state){
     if(localStorage.getItem('access')){
       state.access = localStorage.getItem('access')
      
     }

     else{
       state.access = ''
     }

    },

    setAccess(state, access){
       state.access = access
       localStorage.setItem('access', access)
    },

    setWelcomeMessage(state, message){
      state.namestudent = message
    }

  },

  actions:{
    async login({commit}, {email, password}){
    const response =  await axios.post('http://localhost:3000/api/auth/login/', {
               email,
               password
        })

       const access = response.data.access
       const studentname = response.data.name
       commit('setAccess', access)
       commit('setWelcomeMessage', studentname)         
     },
  },



})

export default store;