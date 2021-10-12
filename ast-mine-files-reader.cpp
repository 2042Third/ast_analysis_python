#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/json_parser.hpp>
#include <map>
#include <iostream>
#include <string>
#include <boost/optional/optional.hpp>
#include<boost/algorithm/string.hpp>

using namespace std;
namespace alg = boost::algorithm;

namespace pt = boost::property_tree;

string get_three(string a){
  alg::ireplace_all(a,".","#");
  vector<string> strs;

  boost::split(strs,a,boost::is_any_of("/"));
  if(strs.size()<3)return "";
  string elem_name = strs[0]+"."+strs[1]+"."+strs[2];
  
  return elem_name;

}

void proj_freq(pt::ptree &out_tree, string a,long int freqc){
  boost::optional<  pt::ptree& > child = out_tree.get_child_optional( "a" );
  if( !child )
  {
    out_tree.put(a,freqc);
  }
  else {
    long int v = out_tree.get<long int>(a);
    v +=freqc;
    out_tree.put(a,v);
  }
}

int main (int argc, char ** argv){
  if (argc != 2) {
    return 0;
  } else {
    std::string usr_input(argv[1], (int) sizeof(argv[1]) / sizeof(char));

    std::ifstream jsonFile(argv[1]);

    pt::ptree propt;
    pt::ptree out_tree;
    long int count = 0, count_file = 0, count_proj = 0;
    pt::read_json(jsonFile, propt);
    for (auto & property: propt) {
      std::cout << property.first << "----\n";
      for (auto & elem:property.second){//file occurence
        string elem_name = elem.first;
        elem_name = get_three(elem_name);
        count_file++;
        long int file_freq =0;
        for (auto & property: elem.second) {//occurence line number
          count++;
          file_freq++;
        }
        proj_freq(out_tree,property.first+"."+elem_name,file_freq);
        // out_tree.put(property.first+"."+elem_name,file_freq);
      }
      std::cout << "\t-"<< count<<" occurences in "<<count_file<<" files" << "\n";
      count = 0;
      count_file = 0;
    }
    write_json("reader_out.json",out_tree);
  }
  return 0;
  
}