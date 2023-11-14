import { createStore } from 'vuex';
import axios from 'axios';

const store =  createStore({
  state: {
  	access: '',
  	refresh: ''
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
  },

  actions:{
  	login({commit}, {email, password}){
  		return new Promise((resolve, reject) => {
  			axios.post('http://localhost:3000/api/auth/login/', {
               email,
               password
  			})
  		    .then(response => {
             const access = response.data.access;
             commit('setAccess', access);
             resolve();
             })
            .catch(error => {
             console.error(error);
             reject(error);
           });
  		})
  	} 
  }
})

export default store;