let app=Vue.createApp({
    data() {
        return {
            greeting: 'Hello Vue!',
            isVisible:false
        }
    },
    methods:{
        toggleBox(){
            this.isVisible=!this.isVisible
        },
        greet(greeting){
            console.log(greeting)
        }
    }
})
app.component('login-form',{
    template:`
        <form @submit.prevent="handleSubmit">
            <h1>{{ title }}</h1>
            <custom-input 
                v-for="(input,i) in inputs"
                :key="i"
                v-model="input.value" 
                :label="input.label"
                :type="input.type"
            />
            
            <button>Log in </button>
        </form>
    `
    // <custom-input v-model="email" v-bind:label="emailLabel"/>
    // <custom-input v-model="password" :label="passwordLabel" />
    ,
    components:['custom-input'],
    data(){
        return{
            title:'Login Form',
            inputs:[
                {
                    label:'Email',
                    value:'',
                    type:'email'
                },
                {
                    label:'Password',
                    value:'',
                    type:'password'
                },
            ],
            email:'',
            password:'',
            emailLabel:'Email',
            passwordLabel:'Password'
        } 
    },
    methods:{
        handleSubmit(){
            // console.log(this.email,this.password)
            console.log(this.inputs[0].value,this.inputs[1].value)
        }
    }
})
app.component('custom-input',{
    template:`
        <label>
            {{ label }}
            
            <input :type="type" v-model="inputValue">
        </label>
    `
    // <input type="text" v-model="inputValue">
    ,
    props:['label','modelValue','type'],
    computed:{
        inputValue:{
            get(){
                return this.modelValue
            },
            set(value){
                // console.log(value)
                this.$emit('update:modelValue' ,value)
            }
        }
    }
    // data(){
    //     return{
    //         inputValue:''
    //     }
    // }
})
app.mount('#app')