<template>
  <ul class="items" aria-label="submenu">
    <li class="item" v-for="(item, idx) in items" :key="idx">
      <a href="#" class="item__link">
        <tg-icon
          v-if="item.icon"
          :name="item.icon"
          class="w-4 h-4 mr-3"
          aria-hidden="true"
        />
        <div class="wrapper">
          <span class="item__link-text">{{ item.title }}</span>
          <span
            class="item__link-badge"
            v-if="item.count"
            :class="{ alert: item.count > 0 }"
          >
            {{ item.count }}
          </span>
        </div>
      </a>
    </li>
  </ul>
</template>

<script>
  export default { props: ["items"] };
</script>

<style lang="scss" scoped>
  @import "@/assets/styles/reusable";

  .items {
    @apply absolute right-0 w-44 p-2 mt-2 space-y-2 rounded-md shadow-md hidden
    text-true-gray-600 bg-warm-gray-100 border border-true-gray-200;
  }
  .item {
    @apply flex;

    &__link {
      @extend %flexInline;
      @apply w-full px-2 py-1.5 text-sm justify-start font-semibold
      font-pt transition-colors duration-150 rounded-md tracking-wider
      hover:bg-warm-gray-200 hover:text-brand-primary;

      &-badge {
        @apply px-2 py-1.5 text-xs font-bold leading-none rounded-full;
      }

      .wrapper {
        @apply inline-flex justify-between items-center w-full;
      }
    }
  }
  .alert {
    @apply text-red-600 bg-red-100;
  }
</style>
