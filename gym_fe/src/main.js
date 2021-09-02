import { createApp } from "vue";
import axios from "axios";

import App from "@/App.vue";
import { router } from "./router";

import "./assets/fonts/index.css";
import "virtual:windi.css";

axios.defaults.baseURL = "http://localhost:8000/";

const app = createApp(App);
app.use(router, axios);
app.mount("#app");
