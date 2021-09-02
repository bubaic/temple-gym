<template>
  <div class="team">
    <Member
      v-for="(m, i) in ourTeam"
      :key="i"
      :name="m.name"
      :role="m.role"
      :img="m.img"
    />
  </div>
</template>

<script>
import { ourTeam } from "@/temp/team-members";
import Member from "./TeamMember.vue";

export default {
  components: { Member },
  setup: () => {
    return { ourTeam };
  },
};
</script>

<style lang="scss" scoped>
@import "@/assets/styles/reusable";

@layer base {
  .team {
    @extend %trans, %flexRow;
    @apply my-6 py-2 justify-evenly flex-wrap gap-4;
  }

  .headtitle {
    @extend .atMobile;
  }
}
</style>
