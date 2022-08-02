ggplot(data, aes(x=IRC, y=`Total Energy [Ha]`)) +
  geom_point() +
  theme_bw() +
  xlim(-4,4)+
  coord_fixed(70)

