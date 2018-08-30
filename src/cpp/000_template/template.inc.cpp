/*
//---------------------------------------------------------------------------//
//              BEGIN COMPETETIVE PROGRAMMING TEMPLATE HEADER
//---------------------------------------------------------------------------//
//---------------------------------------------------------------------------//
INFO :  COMPETETIVE PROGRAMMING TEMPLATE HEADER
AUTH :  Sayan Bhattacharjee (aerosayan)
EMAIL:  aero.sayan@gmail.com
VER  :  1.0.1
//---------------------------------------------------------------------------//
*/


//---------------------------------------------------------------------------//
//                           INCLUDES AND NAMESPACE
//---------------------------------------------------------------------------//
#include<bits/stdc++.h>
using namespace std;


//---------------------------------------------------------------------------//
//                         TYPEDEFS AND TYPE DEFINES
//---------------------------------------------------------------------------//
#define vec vector
#define pqueue priority_queue
#define umap unordered_map
#define uset unordered_set

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;

//---------------------------------------------------------------------------//
//                            NUMERICAL CONSTANTS
//---------------------------------------------------------------------------//
// Infinity in 32 bit integer form and 64 bit long long int form
static const int    INFI  = 0x3f3f3f3f;
static const ll     INFL  = 0x3f3f3f3f3f3f3f3fLL;
static const double PI    = -1.0; // TODO : insert the correct formula 2*arccos(0);



//---------------------------------------------------------------------------//
//                           ACTIVATE DEBUGGING
//---------------------------------------------------------------------------//
// Are we debugging? Comment out the define DEBUG line below if we are not.
// Alternatively, we can also compile with flag -D DEBUG to get the same result

//---------------------------------------------------------------------------//
// MARK ::  __de
//#define DEBUG  // UNCOMMENT THIS LINE TO ACTIVATE DEBUG MODE
//---------------------------------------------------------------------------//


// Safeguard to ensure that we donot submit a debug version to the server
#ifdef DEBUG
// NOTE : \\ at the end of D on line 1 ,it is required to prevent \040 error
// NOTE : The output will be DEBUGGING
bool debugging_banner = cout<<
" ____   _____  _____  _____  _____  _____  _____  _____  _____ \n"
"|    \\ |   __|| __  ||  |  ||   __||   __||     ||   | ||   __|\n"
"|  |  ||   __|| __ -||  |  ||  |  ||  |  ||-   -|| | | ||  |  |\n"
"|____/ |_____||_____||_____||_____||_____||_____||_|___||_____|\n"<<endl;
#endif


//---------------------------------------------------------------------------//
//                       ACTIVATE FAST IO USING CIN
//---------------------------------------------------------------------------//
// Make IO using cin as fast as scanf. But when this is activated we can not
// use scanf or printf. Cin can be made as fast as scanf by switching off synch
#define fastIO() ios::sync_with_stdio(false);cin.tie(NULL)

//---------------------------------------------------------------------------//
//                                MOST USED 
//---------------------------------------------------------------------------//
// begining and ends of STL containers
#define B begin()
#define E end()
// size of STL containers
#define sz size() 
// push back ,emplace back and insert features 
#define eb emplace_back
#define pb push_back
#define ins insert
// newline character to be used instead as cout<<x<<nl; instead of <<endl
#define nl "\n"
// first and second component of a STL pair container
#define X first
#define Y second
// full range description
#define all(CON) (CON).B,(CON).E
#define rall(CON) (CON).E,(CON).E

//---------------------------------------------------------------------------//
//                                DEBUGGING
//---------------------------------------------------------------------------//

// NOTE : WHEN USING MULTI LINE MACROS USE \ AT THE END OF THE DIFFERENT LINES
// WARNING : AND THE / SHOULD BE THE LAST CHARACTER ON THE LINE
// WARNING : EVEN IF A ' ' (SPACE) IS PRESENT AFTER \ THEN IT WILL CAUSE ERRORS
// 
#ifdef DEBUG
#define watch(VAR) {cout<<(#VAR)<<"\t:\t"<<(VAR)<<endl;}

// print containers of STL like vectors, arrays etc
#define dbgc(CON) {cout<<(#CON)<<"\t:\t{";\
	for(size_t i=0;i<(CON).sz;i++){\
		cout<<(CON).at(i)<<",";}cout<<"}"<<endl;}
#define dbgc2(CON) {cout<<(#CON)<<"\t:\t{";\
	for(size_t i=0;i<(CON).sz;i++){\
		if(i!=0) cout<<"\t \t";\
		for(size_t j=0;j<(CON)[i].sz;j++){\
			cout<<(CON)[i][j]<<" ";\
		}cout<<endl;}}


// print standard arrays and matrices
#define dbgarr(ARR,N) { cout<<(#ARR)<<"\t:\t{";\
	for(size_t i=0;i<(N);i++){\
		cout<<(ARR)[i]<<",";}cout<<"}"<<endl;}
#define dbgarr2(ARR,N,M){cout<<(#ARR)<<"\t:\t";\
	for(size_t i=0;i<(N);i++){\
		for(size_t j=0;j<(M);j++){\
			cout<<(ARR)[i][j]<<" ";\
		}cout<<endl;}}

// print a string
#define dbgstr(STR) {cout<<(STR);}
#define dbgs(STR) {cout<<(STR)<<nl;}

// print a horizontal line with n occurances of a character 
#define hrn(N,CHAR) { for(int i=0;i<(N);i++){cout<<(CHAR);}cout<<endl; }
#define hr() hrn(80,'-')

#else
#define watch(VAR) 
#define dbgc(CON) 
#define dbgc2(CON) 
#define dbgarr(ARR,N)
#define dbgarr2(ARR,N,M)
#define dbgstr(STR)
#define dbgs(STR) 
#define hrn(N,CHAR) 
#define hr() 
#endif

//---------------------------------------------------------------------------//
//                                  LOOPS
//---------------------------------------------------------------------------//
//---------------------------
// FOR LOOPS
//---------------------------
// for loops -> less than equal to
#define repl(TYPE,VAR,START,END) for((TYPE) (VAR)=(START);(VAR)<(END);(VAR)++)
#define reple(TYPE,VAR,START,END) for((TYPE) (VAR)=(START);(VAR)<=(END);(VAR)++)
// reverse for loop -> greater than equal to
#define repg(TYPE,VAR,START,END) for((TYPE) (VAR)=(START);(VAR)>(END);(VAR)--)
#define repge(TYPE,VAR,START,END) for((TYPE) (VAR)=(START);(VAR)>=(END);(VAR)--)
// for loop -> default
#define rep(TYPE,VAR,START,END) repl((TYPE),(VAR),(START),(END))
#define rrep(TYPE,VAR,START,END) repge((TYPE),(VAR),(START),(END))


//---------------------------------------------------------------------------//
//              END COMPETETIVE PROGRAMMING TEMPLATE HEADER
//---------------------------------------------------------------------------//

