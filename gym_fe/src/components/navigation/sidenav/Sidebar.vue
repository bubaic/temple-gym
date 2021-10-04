<template>
  <transition name="bar">
    <div class="sidebar" v-if="!isSidebarOpen">
      <div class="wrapper">
        <SidebarItem
          v-for="(i, idx) in items"
          :key="idx"
          :header="i.header"
          :content="i.item"
        />
      </div>
    </div>
  </transition>
</template>

<script>
import SidebarItem from "./SidebarItems.vue";

export default {
  name: "sidebar",
  props: ["isSidebarOpen"],
  components: { SidebarItem },
  data: function () {
    return {
      items: [
        {
          header: "dashboards",
          item: [
            { title: "analytics", icon: "chart-pie" },
            { title: "shop", icon: "" },
          ],
        },
        {
          header: "apps",
          item: [
            { title: "email", icon: "envelope-open-text" },
            { title: "chat", icon: "" },
            { title: "todo", icon: "" },
            { title: "calendar", icon: "" },
          ],
        },
        { header: "reports", item: [{ title: "invoice", icon: "" }] },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>
@import "@/assets/styles/reusable";

.wrapper {
  @extend %flexColumn;
  align-items: start !important;
}

.sidebar {
  @extend %trans;
  // @apply  px-8  top-16
  //   bg-light-400 z-0  z-10 absolute h-screen;

  @apply <sm:absolute bg-light-400 w-60 pl-16 pt-0 border-r
    sm:relative shadow-none overflow-y-auto flex flex-wrap flex-none;
}

/** */
.bar-enter-from,
.bar-leave-to {
  opacity: 0;
  transform: translateX(-10rem);
}
.bar-enter-active,
.bar-leave-active {
  transition: all 250ms cubic-bezier(0.68, -0.55, 0.27, 1.55);
}
.bar-enter-to,
.bar-leave-from {
  opacity: 1;
  transform: translateX(-10rem);
}
/**/

.fad {
  @apply text-xs mr-2 relative -top-px;
}
</style>
