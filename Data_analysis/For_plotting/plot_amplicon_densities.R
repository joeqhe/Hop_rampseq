rm (list = ls (all = TRUE))

require (ggplot2) # Plot stuff
require(stringr) # manipulate strings

input_data_file <- "/Users/joehe/New_cluster_files/hejoe/git_repos/Hop_rampseq/Data_analysis/For_plotting/11542_6815_60-24312_9039_55_amplicon_distribution.csv"
contig_size_data_file <- "/Users/joehe/New_cluster_files/hejoe/git_repos/Hop_rampseq/Data_analysis/For_plotting/contig_sizes.tsv"

amplicon_data <- read.csv (input_data_file, header = FALSE)
contig_sizes <- read.table (contig_size_data_file, sep = "\t", header = FALSE)

primer_pair <- str_split (input_data_file, "/", simplify = TRUE)
primer_pair <- primer_pair [length (primer_pair)]
primer_pair <- unlist (str_split (primer_pair, "\\.", simplify = TRUE)) [1]# need to do this for some reason 
primer_pair <- str_split (primer_pair, "_amplicon", simplify = TRUE) [1]

output_file_name <- paste ("/Users/joehe/New_cluster_files/hejoe/git_repos/Hop_rampseq/Data_analysis/For_plotting/contig_len_", primer_pair, ".jpg")



colnames (amplicon_data) <- c ("contig", "amplicon_count")
amplicon_data$contig <- str_split (amplicon_data$contig, "_", simplify = TRUE) [ ,2]

colnames (contig_sizes) <- c ("contig", "contig_len")

all_data <- merge (amplicon_data, contig_sizes, by.y = "contig" )
all_data$density <- all_data$amplicon_count * 10^6 / all_data$contig_len

all_data$contig <- factor (all_data$contig, levels = all_data$contig [order (all_data$contig_len)])

plot_image <- ggplot (data = all_data, aes (x = contig, y = density)) +
  geom_bar (stat = "identity") +
  ggtitle (paste ("Amplicons for", primer_pair)) +
  coord_cartesian () +
  scale_x_discrete (drop = FALSE) +
  ylab ("density/Mbp^-1") +
  xlab ("Contig") +
  theme (axis.text.x=element_blank ())


ggsave (output_file_name, width = 50, height = 10, units = "cm")

