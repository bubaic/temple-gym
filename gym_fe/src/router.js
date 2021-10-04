import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    /* mains */
    // { path: "/", component: () => import("@/pages/Main") },
    {
      path: "/:notfound(.*)",
      component: () => import("@/pages/errors/404.vue"),
    },
    // { path: "/shop", component: () => import("@/pages/Shop") },

    /* account */
    // { path: "/login", component: () => import("@/pages/Login") },
    // { path: "/sign-up", component: () => import("@/pages/Signup") },

    /* dashboard */
    {
      path: "/dashboard",
      component: () => import("@/pages/dashboard/Dashboard.vue"),
    },

    /* company */
    { path: "/", component: () => import("@/pages/Home.vue") },

    /* membership */

  ],
});

export { router };
