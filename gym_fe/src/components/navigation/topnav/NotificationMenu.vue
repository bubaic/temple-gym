<template>
  <NavPopup :items="items" :class="{ show: isNotifyOpened }" />
</template>

<script>
import NavPopup from "./NavPopup.vue";

export default {
  props: ["isNotifyOpened"],
  components: { NavPopup },
  data() {
    return {
      items: [
        { title: "Messages", count: 13, icon: "" },
        { title: "Sales", count: 0, icon: "" },
        { title: "Alerts", count: 2, icon: "" },
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
