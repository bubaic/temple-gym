<template>
  <NavPopup
    aria-label="submenu"
    :items="items"
    :class="{ show: isSubmenuOpened }"
  />
</template>

<script>
import "@/components/icons/gear";
import "@/components/icons/log-out";
import "@/components/icons/user";
import NavPopup from "./NavPopup.vue";

export default {
  props: ["isSubmenuOpened"],
  components: { NavPopup },
  data() {
    return {
      items: [
        { title: "Profile", count: "", icon: "user" },
        { title: "Settings", count: "", icon: "gear" },
        { title: "Log out", count: "", icon: "logOut" },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>
.show {
  @apply block;
}
</style>
