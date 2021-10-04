<template>
  <section class="data-table">
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>#</th>
            <th>user</th>
            <th>contact</th>
            <th>aadhar</th>
            <th>actions</th>
          </tr>
        </thead>
        <tbody v-for="(v, i) in users" :key="i">
          <tr>
            <td>{{ v.mID }}</td>
            <td>
              <div class="user-infos">
                <div class="img-wrapper">
                  <img loading="lazy" />
                  <div class="img-back" aria-hidden="true"></div>
                </div>
                <div class="details">
                  <p class="details__name">{{ v.name }}</p>
                  <p class="details__other">{{ v.typ }}</p>
                </div>
              </div>
            </td>
            <td>
              <div class="contact" v-for="(c, id) in v.contact" :key="id">
                <span>{{ c }}</span>
              </div>
            </td>
            <td class="font-bold">{{ v.aadhar }}</td>
            <td>
              <div class="actions">
                <button><tg-icon name="bag" /></button>
                <button><tg-icon name="bag" /></button>
                <button><tg-icon name="bag" /></button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>

<script>
  import "@/components/icons/bag";

  export default {
    data: function () {
      return {
        users: [
          {
            mID: 1,
            name: "john doe",
            contact: { addr: "lake ddi", phone: "7758793642" },
            aadhar: "7758-7936-4200",
            typ: "admin",
          },
          {
            mID: 2,
            name: "jane doe",
            contact: { addr: "some address", phone: "7758793642" },
            aadhar: "7758-7936-4200",
            typ: "member",
          },
					 {
            mID: 30,
            name: "p. mathhias",
            contact: { addr: "adresssdslkd 115", phone: "7758793642" },
            aadhar: "7758-7936-4200",
            typ: "staff",
          },
          {
            mID: 30,
            name: "p. mathhias",
            contact: { addr: "adresssdslkd 115", phone: "7758793642" },
            aadhar: "7758-7936-4200",
            typ: "staff",
          },
        ],
      };
    },
  };
</script>

<style lang="scss" scoped>
  @import "@/assets/styles/reusable";

  .data-table {
    @apply w-full overflow-hidden rounded-lg shadow-sm;
  }
  .table-wrapper {
    @apply w-full overflow-x-auto;
  }
  table {
    @apply w-full whitespace-nowrap;

    th,
    td {
      @apply px-4 py-3;
    }

    thead {
      tr {
        @apply text-xs font-semibold tracking-wide text-left uppercase
  				border-b bg-warm-gray-100 text-gray-500;

        th {
          @apply font-poppins;
        }
      }
    }
    tbody {
      @apply bg-white;

      tr {
        @apply text-blue-gray-700 border-b;
      }
    }

    td {
      @apply  text-sm font-pt text-gray-600;
    }
  }
  .contact {
    @extend %flexColumn;
    @apply items-start justify-center;
  }
  .user-infos {
    @extend %flexRow;
    @apply text-sm;

    .img-wrapper {
      @apply relative hidden w-8 h-8 mr-3 rounded-full md:block;

      img {
        @apply object-cover w-full h-full rounded-full p-0.5;
      }
      .img-back {
        @apply absolute inset-0 rounded-full shadow-inner bg-true-gray-100;
      }
    }
    .details {
      @apply font-pt capitalize;

      &__name {
        @apply font-semibold;
      }
      &__other {
        @apply text-xs text-gray-600;
      }
    }
  }
  .actions {
    @extend %flexRow;
    @apply gap-1;

    button {
      @extend %flexRow, %trans;
      @apply bg-warm-gray-100 w-6 h-6 rounded-full justify-center;

      &:hover {
        @apply bg-green-100;

        .fa-icon {
          @apply text-brand-primary;
        }
      }
    }
  }
</style>
