import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    /* mains */
    // { path: "/", component: () => import("@/pages/Main") },
    // { path: "/:notfound(.*)", component: () => import("@/pages/NotFound") },
    // { path: "/shop", component: () => import("@/pages/Shop") },
    // { path: "/pricing", component: () => import("@/pages/PriceTable") },

    /* account */
    // { path: "/login", component: () => import("@/pages/Login") },
    // { path: "/sign-up", component: () => import("@/pages/Signup") },

    /* dashboard */
    {
      path: "/dashboard",
      component: () => import("@/pages/admin/Dashboard.vue"),
    },

    /* company */
    { path: "/", component: () => import("@/pages/Home.vue") },
    { path: "/about", component: () => import("@/pages/About.vue") },
    // { path: "/contact", component: () => import("@/pages/Contact") },
    // { path: "/terms", component: () => import("@/pages/rules/Terms") },
    // { path: "/policy", component: () => import("@/pages/rules/Policy") },

    /* membership */
    // { path: "/info", component: () => import("@/pages/Info") },

    /* quicklink */
    // { path: "/gallery", component: () => import("@/pages/Gallery") },
    // { path: "/videos", component: () => import("@/pages/Videos") },
    // { path: "/faqs", component: () => import("@/pages/qa/Faq") },

    /* section: nested */
    // {
    //   path: "/why-join",
    //   component: () => import("@/layouts/benefits/AllBenefits"),
    // },
  ],
});

export { router };
