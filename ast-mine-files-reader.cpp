#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/json_parser.hpp>
#include <map>
#include <iostream>

namespace pt = boost::property_tree;

int main (int argc, char ** argv){
  if (argc != 2) {
    return 0;
  } else {
    std::string usr_input(argv[1], (int) sizeof(argv[1]) / sizeof(char));

    std::ifstream jsonFile(argv[1]);

    pt::ptree propt;
    long int count = 0, count_file = 0;
    pt::read_json(jsonFile, propt);
    for (auto & property: propt) {
      std::cout << property.first << "----\n";
      for (auto & elem:property.second){
        // std::cout<< "\t"<<elem.first<<"\n\t";
        // std::cout<<elem.second.get_value<std::string>();
        count_file++;
        for (auto & property: elem.second) {
          count++;
            // std::cout <<" "<<property.second.get_value < std::string > ();
        }
        // std::cout<<std::endl;
      }
      std::cout << "\t-"<< count<<" occurences in "<<count_file<<" files" << "\n";
      count = 0;
      count_file = 0;
    }
  }
  return 0;
  
}