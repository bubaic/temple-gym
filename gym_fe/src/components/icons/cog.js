import Icon from "./Icon.vue";
import "@/assets/styles/_keyframes.scss";

var rotate = {
  right: `animation: spin-right 1.2s infinite linear`,
};

Icon.register({
  cog: {
    width: 40,
    height: 24,
    raw: `
      <path
        style="fill:none;stroke:currentColor;stroke-width:1.75;${rotate.right}"
        d="M 31.085233,9.8092034 C 33.894863,12.734406 29.798456,17.70575 26.390024,15.507243 22.820872,13.73299 24.85509,7.6404988 28.853618,8.5480636 l 1.22696,0.4338795 z M 20.408726,6.3048209 c -0.878778,-1.4840876 0.646367,-3.4769101 2.299873,-3.1061811 1.406832,0.7063041 3.510099,1.4058136 4.191906,-0.6881986 0.428726,-1.6709383 2.916506,-2.00145167 3.824208,-0.5701963 0.496186,1.4931096 1.487606,3.4740385 3.449782,2.4771009 1.484089,-0.8787778 3.47691,0.646366 3.106181,2.2998722 -0.706301,1.4068327 -1.405811,3.5101 0.6882,4.191905 1.670938,0.428726 2.00145,2.916506 0.570194,3.824212 -1.493108,0.496182 -3.474037,1.487601 -2.4771,3.44978 0.878777,1.484088 -0.646367,3.476909 -2.299872,3.106181 -1.406833,-0.706302 -3.510099,-1.40581 -4.191906,0.688199 -0.428726,1.670938 -2.916506,2.001453 -3.824209,0.570196 -0.318438,-1.778738 -1.948737,-3.526872 -3.82672,-2.324569 -1.594509,0.567938 -3.291046,-1.25946 -2.628255,-2.809187 1.431883,-1.582751 0.371636,-3.692162 -1.482467,-4.20155 -1.361315,-0.99515 -0.857506,-3.4429904 0.818029,-3.7667814 1.491474,-0.086344 2.50952,-1.8144429 1.782156,-3.1407827 z"
      />
      <path
        style="fill:none;stroke:currentColor;stroke-width:1.5"
        d="M 10.726427,8.0346456 C 11.099917,10.712703 6.9442571,11.795579 5.9633048,9.275813 4.7296927,6.9223023 8.2101365,4.4277636 10.014455,6.4811468 l 0.492908,0.7139971 z M 6.3313736,1.9681115 c 0.1057083,-1.14496491 1.7084018,-1.62477463 2.456329,-0.7781107 0.4835263,0.9314268 1.3457734,2.1314709 2.5326394,1.2673003 0.884797,-0.7346636 2.357385,0.059515 2.287952,1.1872604 -0.315831,1.0002532 -0.554965,2.457546 0.894358,2.6863703 1.144964,0.1057075 1.624775,1.7084005 0.77811,2.4563278 -0.931425,0.4835259 -2.131469,1.3457734 -1.2673,2.5326394 0.734663,0.884796 -0.05952,2.357384 -1.187261,2.287951 -1.000254,-0.315831 -2.457545,-0.554966 -2.686369,0.894358 -0.105709,1.144965 -1.708402,1.624774 -2.4563298,0.77811 C 7.1999768,14.348893 6.3377292,13.148848 5.1508641,14.013017 4.266067,14.747682 2.793479,13.953497 2.8629126,12.825758 3.3863977,11.740763 3.1895282,10.159393 1.7053778,10.074383 0.62231587,9.7576524 0.42067097,8.1075848 1.3844675,7.5298852 2.7764773,7.235047 3.0286776,5.6814669 2.2266455,4.6815027 1.8806282,3.6118983 3.1097162,2.4870734 4.1410749,2.9673173 c 0.8391336,0.536501 2.0645034,0.00138 2.1902987,-0.9992058 z"
      />
    `,
  },
});
