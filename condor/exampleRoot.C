{
TFile f("input_file.root");
output_ntuples = process(f); // do some calculation
TFile g("output_file.root", "w");
g.write(output_ntuples);
}