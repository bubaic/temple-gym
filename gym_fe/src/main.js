import { createApp } from "vue";
import axios from "axios";

import App from "@/App.vue";
import { router } from "./router";

import Icon from "@/components/icons/Icon.vue";
import "./assets/fonts/index.css";
import "virtual:windi.css";

axios.defaults.baseURL = "http://localhost:8000/";



const app = createApp(App);
app.component("tg-icon", Icon);
app.use(router, axios);
app.mount("#app");
